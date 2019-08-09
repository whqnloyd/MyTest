from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Activation, Flatten, Dropout
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
import tensorflow as tf
import numpy as np
import glob
import cv2

(h, w) = (80, 40)

# frozen_graph = freeze_session(K.get_session(), output_names=[out.op.name for out in model.outputs])
# tf.train.write_graph(frozen_graph, "C:/Users/LR Admin/Documents/VPick/data/Test Data/All/", "newModel.pb", as_text=False)
def freeze_session(session, keep_var_names=None, output_names=None, clear_devices=True):
    graph = session.graph
    with graph.as_default():
        freeze_var_names = list(set(v.op.name for v in tf.global_variables()).difference(keep_var_names or []))
        output_names = output_names or []
        output_names += [v.op.name for v in tf.global_variables()]
        input_graph_def = graph.as_graph_def()
        if clear_devices:
            for node in input_graph_def.node:
                node.device = ""
        frozen_graph = tf.graph_util.convert_variables_to_constants(
            session, input_graph_def, output_names, freeze_var_names)
        return frozen_graph

def createModel(dense=2, finalActiv='softmax'):
    layers = [9, 18, 36, 72, 144, 288, 576]
    i = 0

    model = Sequential()
    for layer in layers:
        i += 1
        model.add(Conv2D(filters=layer, kernel_size=(3, 3), input_shape=(h, w, 1), padding='same'))
        model.add(Activation('relu'))
        if i % 3 == 0:
            model.add(MaxPooling2D(pool_size=2))
            i = 0

    model.add(Dropout(0.1))
    model.add(Flatten())
    model.add(Dense(layers[-1]))
    model.add(Activation('relu'))
    model.add(Dense(dense, activation=finalActiv))
    print(model.summary())
    return model

def train(trainPath, trainSize, e=30):
    data = np.loadtxt(trainPath, dtype=np.float32, delimiter=',')
    # X = data[:, :1728]
    # Y = data[:, 1728:]
    # X = np.reshape(X, (-1, h, w, 1))
    xTrain = np.reshape(data[:2380, :h*w], (-1, h, w, 1))
    xVal = np.reshape(data[2380:2630, :h*w], (-1, h, w, 1))
    xTest = np.reshape(data[2630:2881, :h*w], (-1, h, w, 1))
    yTrain = data[:2380, h*w:]
    yVal = data[2380:2630, h*w:]
    yTest = data[2630:2881, h*w:]

    model = createModel()
    opt = Adam(lr=0.000001)
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])
    model.fit(xTrain, yTrain, batch_size=trainSize, epochs=e, validation_data=(xVal, yVal), verbose=2)
    score = model.evaluate(xTest, yTest, verbose=0)
    print("Test Data Accuracy:", score[1])

    key = input('Do you want to save this result? (y/n):')
    if key == 'y':
        model.save_weights(modelPath, overwrite=True)
        print('Model saved')

def trainIncremental(trainPath, modelPath, trainSize=20):
    trainGen = ImageDataGenerator(rescale=1. / 255)
    valGen = ImageDataGenerator(rescale=1 / .255)
    testGen = ImageDataGenerator(rescale=1. / 255)

    train_generator = trainGen.flow_from_directory(trainPath + "Train", color_mode="grayscale", target_size=(h, w),
                                                   shuffle=True, batch_size=20, class_mode='binary', )
    val_generator = valGen.flow_from_directory(trainPath + "Val", color_mode="grayscale", target_size=(h, w),
                                               batch_size=20, class_mode='binary', )
    test_generator = testGen.flow_from_directory(trainPath + "Val", color_mode="grayscale", target_size=(h, w),
                                                 batch_size=20, class_mode='binary', )
    totalTrain = 3320
    totalVal = 500
    totalTest = 500

    model = createModel(dense=1, finalActiv='sigmoid')
    opt = Adam(lr=0.000001)
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])

    model.fit_generator(train_generator, samples_per_epoch=totalTrain,
                        validation_data=val_generator, validation_steps=totalVal // trainSize, epochs=30)
    score = model.evaluate_generator(test_generator, totalTest)
    print("Test Data Accuracy:", score[1])

    key = input('Do you want to save this result? (y/n):')
    if key == 'y':
        model.save_weights(modelPath, overwrite=True)
        print("You're armed with a new model! Now go win that USPS contract!")

def predictAll(predictPath, Inc):
    dist = ["1m", "1.25m", "1.5m", "2m", "2.5m", "3m"]
    types = ["Neutral", "Bright", "Dark", "Mixed"]
    # dist = ["1.25m"]
    # types = ["Dark"]
    if Inc:
        model = createModel(dense=1, finalActiv='sigmoid')
    else:
        model = createModel()
    model.load_weights(modelPath)
    i = -1
    accuracy = [0] * 24

    for d in dist:
        for type in types:
            i += 1
            path = predictPath + d + "/Both/" + type + "/"
            file_list = glob.glob(path + "*.jpg")

            truePos = 0
            longAsDouble = 0
            doubleAsLong = 0
            for file in file_list:
                file.replace('\\', '/')
                file_num = file.split('\\')[-1][:-4]
                if int(file_num) <= 120:
                    y_true = 0              # 0 = LONG
                else:
                    y_true = 1              # 1 = DOUBLE

                input = cv2.imread(file, 0)
                input = cv2.resize(input, (w, h), interpolation=cv2.INTER_CUBIC)
                input = np.reshape(input, (-1, h, w, 1))
                output = model.predict(input)
                #key = np.argmax(output)

                if y_true == output:
                    truePos += 1
                else:
                    #print(str(file_num) + ": " + str(y_true) + "/" + str(key), output)
                    if y_true == 0:
                        longAsDouble += 1
                    else:
                        doubleAsLong += 1

            accuracy[i] = truePos * 100 / 240
            if accuracy[i] < 50.0:
                accuracy[i] = 100 - accuracy[i]
                doubleAsLong = 120 - doubleAsLong
                longAsDouble = 120 - longAsDouble
            print(d + " - " + type + ": " + str(np.round(accuracy[i], decimals=2)) + "%, "
                  + str(doubleAsLong) + ", " + str(longAsDouble))
            # print("Accuracy: " + str(accuracy * 100) + "%")
            # print("Number of times double was mistaken as long: " + str(doubleAsLong))
            # print("Number of times long was mistaken as double: " + str(longAsDouble))
    print("Average accuracy: " + str(np.round(sum(accuracy) / len(accuracy), decimals=2)))

def predict(image, Inc):
    if Inc:
        model = createModel(dense=1, finalActiv='sigmoid')
    else:
        model = createModel()
    model.load_weights(modelPath)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if image.shape[0] != h or image.shape[1] != w:
        image = cv2.resize(image, (w, h), interpolation=cv2.INTER_CUBIC)
        image = np.reshape(image, (1, h, w, 1))

    output = model.predict(image)
    if output == 1:
        print("Predicting LONG")
    else:
        print("Predicting DOUBLE")

if __name__ == "__main__":
    modelPath = "C:/Users/LR Admin/Documents/VPick/data/Test Data/All/7Layer1Dropout_4320(80,40)_98.78.hdf5"
    csvPath = "C:/Users/LR Admin/Documents/VPick/data/Test Data/All/Mixed - 2880 Samples (96x48).csv"
    dataPath = "C:/Users/LR Admin/Documents/VPick/data/Test Data/All/"
    trainSize = 10
    predictPath = "C:/Users/LR Admin/Documents/VPick/data/Big Test Data/1.75m/Long/Train/4.jpg"
    #train(csvPath, trainSize)
    #trainIncremental(dataPath, modelPath, trainSize)
    #predictAll(predictPath, Inc=True)
    predict(cv2.imread(predictPath), Inc=True)
