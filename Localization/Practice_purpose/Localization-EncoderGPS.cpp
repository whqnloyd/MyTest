// Localization-EncoderGPS.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include "Pose_Estimation.h"

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	// Initialization
	vector<enc_data> enc;
	enc_data temp_enc;

	vector<GPS_data> gps_d;
	GPS_data temp_gps;

	ifstream fin_enc("C:\\Users\\jxj115020\\OneDrive\\Localization_encoder_GPS\\Localization-EncoderGPS\\Data_Encoder\\20120229_180327_Wheel.txt");
	ifstream fin_GPS("C:\\Users\\jxj115020\\OneDrive\\Localization_encoder_GPS\\Localization-EncoderGPS\\Data_Encoder\\20120229_180327_GPS.txt");

	ofstream fout ("output.txt");
	// end of Initialization

	
	// encoder value reading from file
	while(1){
		if(fin_enc.eof())	break;

		fin_enc >> temp_enc.t >> temp_enc.v1 >> temp_enc.v2 >> temp_enc.v3 >> temp_enc.v4 ;
		enc.push_back(temp_enc);
		
	}

	// GPS data reading from file
	while(1){
		if(fin_GPS.eof()){
			break;
		}

		fin_GPS >> temp_gps.t >> temp_gps.x >> temp_gps.y >> temp_gps.GPS_mode >> temp_gps.sat_number ;
		gps_d.push_back(temp_gps);
	}

	// 
	int j=0;
	while ( gps_d[j].t < enc[0].t ){
		j++;
		cout << gps_d[j].t << "\t" << enc[0].t << endl;
	}

		// Localization
	Pose_Estimation PE;
	Robot_Pose RP;
	MatrixXd P(3,3);

	for(int k=0; k < (int)(enc.size()) ; k++  ){
		
		cout << "k=>"<<k << endl;
 		PE.Get_Robot_Covariance(P);
		/*Print out covariance data*/
		/*
 		cout << "cov" << endl;
 		cout << P(0,0) << "\t"<< P(0,1) << "\t" << P(0,2) << endl;
 		cout << P(1,0) << "\t"<< P(1,1) << "\t" << P(1,2) << endl;
 		cout << P(2,0) << "\t"<< P(2,1) << "\t" << P(2,2) << endl;		
		*/
		PE.Prediction_by_Odometry( enc[k] );

// 		RP = PE.Get_Robot_Pose();
// 		cout << RP.x << "\t" << RP.y << "\t" << RP.theta << endl;
		
		if( gps_d[j].t < enc[k].t ){
			PE.Update_by_GPS( gps_d[j] );
			j++;
		}

		RP = PE.Get_Robot_Pose();
		//cout<< RP.x << "\t" << RP.y << "\t" << RP.theta << endl; // print out the robot's state or pose
		fout << RP.x << "\t" << RP.y << "\t" << RP.theta << endl;  // save the robot's state or pose		
		
		PE.Get_Robot_Covariance(P);
		/* Print out covariance data
		cout << "cov" << endl;
 		cout << P(0,0) << "\t"<< P(0,1) << "\t" << P(0,2) << endl;
 		cout << P(1,0) << "\t"<< P(1,1) << "\t" << P(1,2) << endl;
 		cout << P(2,0) << "\t"<< P(2,1) << "\t" << P(2,2) << endl;
		*/


	}

	
// 	// temp for file reading check
// 	for(int i=0;i<10;i++){
// 		cout << gps_d[i].t << "\t" << gps_d[i].x << "\t" << gps_d[i].y << "\t" << gps_d[i].GPS_mode << "\t" << gps_d[i].sat_number <<  endl;
// 	}
	


	// close program

	fin_enc.close();
	fin_GPS.close();	
	fout.close();

	return 0;
}

