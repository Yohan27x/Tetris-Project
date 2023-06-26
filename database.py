import csv

class Database:
    def __init__(self):
        pass
                      
    def append(self, user_name, score, mode):
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([str(user_name), str(score), str(mode)])

    def display(self):
        with open('users.csv', 'r', newline='') as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

    def get_best_score(self, user_name):
        with open('users.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            data_user = []
            
            for row in reader:
                if(row[0] == user_name):
                    row[1] = int(row[1])
                    print("row :", row)
                    data_user.append(row)

            for iter_num in range(len(data_user)-1,0,-1):
                for idx in range(iter_num):
                    print("index : ", idx)
                    if data_user[idx][1]>data_user[idx+1][1]:
                        temp1 = data_user[idx][1]
                        temp2 = data_user[idx][2]
                        data_user[idx][1] = data_user[idx+1][1]
                        data_user[idx][2] = data_user[idx+1][2]
                        data_user[idx+1][1] = temp1
                        data_user[idx+1][2] = temp2
                        print("data_user : ", data_user)

            print("data user :", data_user)
            best_scores = []
            i = len(data_user) - 1
            while(i >= 0 and len(best_scores) < 5):
                best_scores.append(data_user[i])
                i -= 1

            print("best_scores :", best_scores)

            return best_scores

            
            

            
                

        
        

            

       
           

                            

