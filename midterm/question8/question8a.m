% Load the pre-trained GoogLeNet model
net = googlenet;

% Get input size and class names
inputSize = net.Layers(1).InputSize;
classNames = net.Layers(end).ClassNames;

% Specify the folder containing the images
folderPath = 'D:\Users\Mason Francis\Downloads\indoorCVPR_09\Images\toystore'; % Replace with the actual path

% List all image files in the specified folder
imageFiles = dir(fullfile(folderPath, '*.jpg')); % Assuming images are in PNG format, you can adjust the extension

% Loop through each image and classify
for i = 1:numel(imageFiles)
    % Read the image
    imagePath = fullfile(folderPath, imageFiles(i).name);
    I = imread(imagePath);
    
    % Resize the image to match the network's input size
    I = imresize(I, inputSize(1:2));
    
    % Classify the image
    [label, scores] = classify(net, I);
    
    % Display the result
    fprintf('Image: %s, Predicted Label: %s\n', imageFiles(i).name, label);
end
