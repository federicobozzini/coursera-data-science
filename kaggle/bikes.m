%% Polyfeatures!
p=4;

loadBasicFile = false;
if loadBasicFile
    featuresIndexes = 2:9;
    yIndex = 12;
    trainFile = 'train.csv';
    testFile = 'test.csv';
else
    featuresIndexes = [3,4, 11:13];
    yIndex = 16;
    trainFile = 'train2.csv';
    testFile = 'test2.csv';
endif


%% Load training data
data = csvread(trainFile);

%% exclude the header
data = data(2:end,:);

dates = data(:, 1);
X = data(:, featuresIndexes);
y = data(:, yIndex);
m = length(y);


X = polyFeatures(X, p);

% Add intercept term to X
X = [ones(m, 1) X];

% Calculate the parameters from the normal equation
theta = normalEqn(X, y);

%% load test data
testdata = csvread(testFile);

%% exclude the header
testdata = testdata(2:end, :);

dates = testdata(:, 1);
mtest = length(dates);
Xtest = testdata(:, featuresIndexes);
Xtest = polyFeatures(Xtest, p);

Xtest = [ones(mtest, 1) Xtest];

ytest = int16(Xtest*theta);
ytest(ytest<0) = 0;
res = ytest;

%% plotting some results
hist(y);
hold on;
hist(ytest, "facecolor", "r");
legend('train data distribution','test data distribution','location','southoutside',...
 'orientation','horizontal');
 title('Distributions the train data and test data');

%%writing the csv file (missing the header, and the dates are wrong)
csvwrite('submit.csv', res);

