#pragma once
#ifdef GARY_MIX_EXPORTS
#define GARY_MIX_API _declspec(dllexport)
#else
#define GARY_MIX_API _declspec(dllimport)
#endif

void GARY_MIX_API GrayDepthSeperate();