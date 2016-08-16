if ~isdeployed
    addpath('brox_OF');
end
%% -------PARAMETERS---------------
param=[];
param.impath = 'ADBSZU/images' ;% input images path (one folder per video)
param.imext = '.jpg' ;% input image extension type
param.cachepath = 'cache';% cache folder path

%% get video names
video_names = dir(param.impath);
video_names={video_names.name};
video_names=video_names(~ismember(video_names,{'.','..'}));
%% create cache folder
if ~exist(param.cachepath,'dir'); mkdir(param.cachepath) ; end 

%% compute optical flow between adjacent frames
extract_OpticalFlow(video_names,param); 