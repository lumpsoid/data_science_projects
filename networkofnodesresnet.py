from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras import losses
from tensorflow.keras.metrics import MeanAbsoluteError
import pandas as pd


def load_train(path):
    df = pd.read_csv(path+'labels.csv')
    datagen_train = ImageDataGenerator(validation_split=0.25,
                                        rescale=1/255.,
                                        horizontal_flip=True)
    datagen_flow_train = datagen_train.flow_from_dataframe(dataframe=df,
                                               directory=path+'/final_files',
                                               x_col="file_name",
                                               y_col='real_age',
                                               class_mode='raw',
                                               subset='training',
                                               batch_size=32,
                                               seed=12345)
    return datagen_flow_train


def load_test(path):
    df = pd.read_csv(path+'labels.csv')
    datagen_test = ImageDataGenerator(validation_split=0.25,
                                      rescale=1/255.)

    datagen_flow_test = datagen_test.flow_from_dataframe(dataframe=df,
                                               directory=path+'/final_files',
                                               x_col="file_name",
                                               y_col='real_age',
                                               class_mode='raw',
                                               subset='validation',
                                               batch_size=32,
                                               seed=12345)
    return datagen_flow_test


def create_model(input_shape):
    optimizer = Adam(lr=0.0001)
    backbone = ResNet50(input_shape=input_shape,
                        weights='/datasets/keras_models/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5',
                        include_top=False)

    model = Sequential()
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Dense(units=1, activation='relu'))

    model.compile(optimizer=optimizer, loss='mean_absolute_error',
                  metrics=[MeanAbsoluteError()])
    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=6,
                steps_per_epoch=None, validation_steps=None):

    model.fit(train_data,
              validation_data=(test_data),
              batch_size=batch_size, epochs=epochs,
              steps_per_epoch=steps_per_epoch,
              validation_steps=validation_steps,
              verbose=2, shuffle=True)
    return model