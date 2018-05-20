import matplotlib.pyplot as plt
import skimage.io

def my_key(pathAndScore):
    return float(pathAndScore.split(' ')[-1])

def getSortedList(scoreList):
    scoreListFile = open(scoreList)
    line = scoreListFile.readline().strip()
    pathAndScore_list = []
    count_image = 0
    while line:
        pathAndScore_list.append(line)
        count_image+=1
        line = scoreListFile.readline().strip()
    print('total images: '+str(len(pathAndScore_list)))
    pathAndScore_list.sort(key=my_key)
    return pathAndScore_list,count_image

def getListByRatio(pathAndScore_list, beginRatio, length, count):
    beginIndex = int(count*beginRatio)
    endIndex = beginIndex+length
    if endIndex > count-1:
        endIndex = count-1
    targetPathAndScorelist = pathAndScore_list[beginIndex:endIndex]
    print('beginIndex: '+ str(beginIndex))
    print('endIndex: '+str(endIndex))
    return targetPathAndScorelist

def getListByScore(pathAndScore_list, beginScore, length, count):
    for cur_index in range(count):
        cur_score = float(pathAndScore_list[cur_index].split(' ')[-1])
        if cur_score >= beginScore:
            beginIndex = cur_index
            endIndex = beginIndex + length
            image_num_large_score = count-cur_index
            print('the number of images which get a score more than '+str(beginScore)+' is ' +str(image_num_large_score))
            print('beginIndex: '+ str(beginIndex))
            print('endIndex: '+str(endIndex))
            return pathAndScore_list[beginIndex:endIndex]
            
def getListByIndex(pathAndScore_list, beginIndex, length, count):
    endIndex = beginIndex + length
    print('beginIndex: '+ str(beginIndex))
    print('endIndex: '+str(endIndex))
    targetPathAndScorelist = pathAndScore_list[beginIndex:endIndex]
    return targetPathAndScorelist
    
def visualize(pathAndScorelist, imageRow, imageCol):
    plt.figure(figsize=(16,12))
    count=1
    for cur_item in pathAndScorelist:
        cur_path = cur_item.split(' ')[0]
        cur_score = cur_item.split(' ')[-1]
        plt.subplot(imageRow, imageCol, count)
        image = skimage.io.imread(cur_path)
        plt.imshow(image)
        plt.text(0, 1, '%s'%(cur_score) , color='black', backgroundcolor='white', fontsize=8)
        plt.axis('off')
        count+=1
    plt.show()
    
if __name__ == '__main__':
    scoreList = '/media/sensetime/416390f3-2e6b-4389-8767-4aaf93e9e9b9/huitu/face_test_gaoqing.out'
    #scoreList = '/media/sensetime/416390f3-2e6b-4389-8767-4aaf93e9e9b9/huitu/face_test_selfi.out'
    startRatio = 0.999
    beginScore = 0.7

    #show setting
    image_num = 30
    show_image_row = 5
    show_image_col = 6
    
    pathAndScore_list, count_all_image = getSortedList(scoreList)
    '''
    #getListByRatio
    targetPathAndScorelist = getListByRatio(pathAndScore_list, startRatio, image_num, count_all_image)
    visualize(targetPathAndScorelist, show_image_row, show_image_col)
    '''
    '''
    #getListByScore
    targetPathAndScorelist = getListByScore(pathAndScore_list, beginScore, image_num, count_all_image)
    visualize(targetPathAndScorelist, show_image_row, show_image_col)
    '''
    #getListByIndex
    beginIndex = 93000
    targetPathAndScorelist = getListByIndex(pathAndScore_list, beginIndex, image_num, count_all_image)
    visualize(targetPathAndScorelist, show_image_row, show_image_col)
    
    
