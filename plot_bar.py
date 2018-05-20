#coding:utf-8 
import matplotlib.pyplot as plt
import numpy as np

def plot_dataset_histogram(selfiList, gaoqingList, color):
    selfiListFile = open(selfiList)
    gaoqingListFile = open(gaoqingList)
    selfiScoreList = []
    gaoqingScoreList = []

    selfiLine = selfiListFile.readline().strip()
    while selfiLine:
        selfiScoreList.append(float(selfiLine.split(' ')[-1]))
        selfiLine = selfiListFile.readline().strip()

    gaoqingLine = gaoqingListFile.readline().strip()
    while gaoqingLine:
        gaoqingScoreList.append(float(gaoqingLine.split(' ')[-1]))
        gaoqingLine = gaoqingListFile.readline().strip()
        
    plt.figure(figsize=(16,8))
    plt.subplot(1,2,1)
    plt.title('life photo')
    n, bins, patches = plt.hist(np.asarray(selfiScoreList), 100, facecolor=color, alpha=0.75)
    plt.subplot(1,2,2)
    plt.title('gao qing')
    n, bins, patches = plt.hist(np.asarray(gaoqingScoreList), 100, facecolor=color, alpha=0.75)
    plt.show()
    
if __name__ =='__main__':
    plot_dataset_histogram('/Users/wangjun/lustre/sdk_face_score/face_test_selfi.out', '/Users/wangjun/lustre/sdk_face_score/face_test_gaoqing.out', 'blue')
