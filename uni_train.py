import tensorflow as tf
import numpy as np
import pandas as pd

def train_and_save_model():
    # 데이터 불러오기
    data = pd.read_csv('gpascore.csv')
    data = data.dropna()

    # 입력 데이터 및 타깃 데이터 준비
    x_data = data[['gre', 'gpa', 'rank']].values
    y_data = data['admit'].values

    # 모델 구성
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='tanh'),
        tf.keras.layers.Dense(128, activation='tanh'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # 모델 컴파일
    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01), loss='binary_crossentropy', metrics=['accuracy'])

    # 모델 학습
    history = model.fit(x_data, y_data, epochs=3000)

    # 학습된 모델 저장
    model.save('my_model.h5')

train_and_save_model()