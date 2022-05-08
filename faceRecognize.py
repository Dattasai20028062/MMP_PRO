from ourPackages import cv, face_recognition, pd, np, csv

data_comp = pd.read_csv("dataBase/dataSet.csv", dtype={'Name': str, 'E_values': float})


class FC:

    @staticmethod
    def encode(image):
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        encoded = face_recognition.face_encodings(image)[0]
        return encoded

    @staticmethod
    def find_loc(img):
        return face_recognition.face_locations(img)

    def image_find(self, img):
        ENC_I = []
        Loc = self.find_loc(img)[0]
        enc_Img = self.encode(img)
        Val = data_comp.iloc[:, 1].values
        Val = csv.reader(Val)
        Name = data_comp.iloc[:, 0].values
        for x in Val:
            F_val = []
            for n in x:
                n = float(n)
                n = round(n, 8)
                F_val.append(n)
            F_val = np.array(F_val)
            ENC_I.append(F_val)

        R = face_recognition.compare_faces(ENC_I, enc_Img)
        Dis = face_recognition.face_distance(ENC_I, enc_Img)
        F_I = np.argmin(Dis)
        try:
            if R[F_I]:
                Y1, X2, Y2, X1 = Loc
                cv.rectangle(img, (X1, Y1), (X2, Y2), (0, 255, 0), 2)
                cv.rectangle(img, (X1, Y2 - 35), (X2, Y2), (0, 255, 0), -1)
                cv.putText(img, Name[F_I], (X1 + 6, Y2 - 6), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv.putText(img, f'{round(Dis[F_I], 2)}', (8, 25), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            else:
                print("Sorry, Image Not Found In our Data Base .. !")
                return
        except IndexError:
            print("ERROR")
        cv.imshow("Image", img)
        cv.waitKey(0)

    def start_rec(self, port):
        cap = cv.VideoCapture(port, cv.CAP_DSHOW)
        ENC_I = []
        Val = data_comp.iloc[:, 1].values
        Val = csv.reader(Val)
        Name = data_comp.iloc[:, 0].values
        for x in Val:
            F_val = []
            for n in x:
                n = float(n)
                n = round(n, 8)
                F_val.append(n)
            F_val = np.array(F_val)
            ENC_I.append(F_val)
        while True:
            ret, img = cap.read()
            S_Img = cv.resize(img, (0, 0), None, fx=0.25, fy=0.25)
            S_Img = cv.cvtColor(S_Img, cv.COLOR_BGR2RGB)
            Loc = self.find_loc(S_Img)
            enc_Img = face_recognition.face_encodings(S_Img, Loc)
            for encodeFace, Faces in zip(enc_Img, Loc):
                R = face_recognition.compare_faces(ENC_I, encodeFace)
                print(R)
                Dis = face_recognition.face_distance(ENC_I, encodeFace)
                F_I = np.argmin(Dis)
                print(Dis)
                try:
                    if R[F_I]:
                        Y1, X2, Y2, X1 = Faces
                        Y1, X2, Y2, X1 = Y1 * 3, X2 * 4, Y2 * 4, X1 * 3
                        cv.rectangle(img, (X1, Y1), (X2, Y2), (0, 255, 0), 2)
                        cv.rectangle(img, (X1, Y2 - 35), (X2, Y2), (0, 255, 0), -1)
                        cv.putText(img, Name[F_I], (X1 + 6, Y2 - 6), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                except IndexError:
                    print("ERROR")
            cv.imshow("Images", img)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break
