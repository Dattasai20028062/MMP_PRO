from ourPackages import os, cv, pd, FC, time


class updateDatabase:
    def __init__(self):
        self.data_path = "dataBase/dataSet.csv"
        self.data = pd.read_csv(self.data_path)
        self.img_path = "imageData"

    def update(self):
        image = []
        N_Image = os.listdir(self.img_path)
        for i in N_Image:
            i = os.path.splitext(i)[0]
            image.append(i)
        data = self.data.iloc[:, 0].values
        for img in image:
            if img not in data:
                pre_img = cv.imread(f'{self.img_path}/{N_Image[image.index(img)]}')
                E_values = FC.encode(pre_img)
                L = ""
                i = 0
                for val in E_values:
                    L += str(val)
                    if val != E_values[-1]:
                        L += ","
                    i += 1
                print(i)
                data_a = [[img, L]]
                df = pd.DataFrame(data_a)
                df.to_csv(self.data_path, mode='a', index=False, header=False)

    def checkUpdate(self):
        if len(os.listdir(self.img_path)) == len(self.data):
            print("You are good to go database is updated ..... : )")
            time.sleep(1)
            return 0
        else:
            print((len(os.listdir(self.img_path)) - len(self.data)), " updates were available")
            return 1
