
import math
import matplotlib.pyplot as plt
import numpy as np

#taking the given file as input 

c_rawdata = np.genfromtxt('clean.txt', dtype=np.int64)
n_rawdata = np.genfromtxt('noise.txt', dtype=np.int64)

#Checking if it is converted to an array 

print(type(c_rawdata))
print(type(n_rawdata))

c_rawdata #Clean data

n_rawdata #noisy data

#Ploting the raw data to see the trend 

# plt.plot(c_rawdata, 'r--')
# plt.show()

# #Ploting the raw data to see the trend 

# plt.plot(n_rawdata, 'g--.')
# plt.show()

len(c_rawdata)

len(n_rawdata)

def func2(image):
    def median_filter(data, filter_size):
        temp = []
        indexer = filter_size // 2
        data_final = []
        data_final = np.zeros((len(data),len(data[0])))
        for i in range(len(data)):

            for j in range(len(data[0])):

                for z in range(filter_size):
                    if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(data[i + z - indexer][j + k - indexer])

                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []
        return data_final

    from PIL import Image

    #uploading image
    img = Image.open(image)

    #Converting to array
    data = np.array(img)

    #Checking noisy image
    img

    #noisy image converted to array
    
    data

    #applying the filter

    clean_data = median_filter(data, 9)

    #See the changes

    clean_data

    # Array to image

    clean_image = Image.fromarray(clean_data)

    ## Original Noisy Image Arrays



    #After denoising 

    plt.plot(clean_data, 'g--')
    plt.show()

## Final result of the image


"""### Gaussian Filtering ###"""

