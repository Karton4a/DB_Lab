import msvcrt # windows only


class console_view():
    def __init__(self, model,controller):
        self.__is_running = True;
        self.__model = model
        self.__controller = controller

    def quit(self):
        return None

    def print_message(self,message,callback = None):
        print(message)
        if callback is not None:
            return callback
        return None

    def print_table(self,table,callback = None):
        print(table[0])
        for row in table[1]:
            print(row)
        if callback is not None:
            return callback
        return None

    def get_input(self,callback = None):
        inp = input()
        if callback is not None:
            pass

    def main_menu(self):
        print('choose what do you want')
        print('1 : show data')
        print('2 : insert data')
        print('3 : remove data')
        print('4 : change data')
        print('5 : generate data')
        print('6 : make querry')
        print('q : quit')
        char = chr(msvcrt.getch()[0])
        return self.__controller.main_menu(char)

    def show_menu(self):
        print("SHOW MENU")
        table_names = self.__model.get_table_names()
        print('type table name or quit')
        print('suppored tables')
        print(table_names)
        answer = input()
        return self.__controller.show_menu(answer)
    
    def choose_delete_menu(self):
        print("DELETE MENU")
        table_names = self.__model.get_table_names()
        print('type table name','suppored tables',table_names)
        answer = input()
        return self.__controller.choose_delete_menu(answer)

    def choose_insert_menu(self):
        print("INSERT MENU")
        table_names = self.__model.get_table_names()
        print('type table name','suppored tables',table_names)
        answer = input()
        return self.__controller.choose_insert_menu(answer)

    def choose_change_menu(self):
        print("CHANGE MENU")
        table_names = self.__model.get_table_names()
        print('type table name','suppored tables',table_names)
        answer = input()
        return self.__controller.choose_change_menu(answer)

    def choose_generate_menu(self):
        print("GENERATE MENU")
        table_names = self.__model.get_table_names()
        print('type table name','suppored tables',table_names)
        answer = input()
        return self.__controller.choose_generate_menu(answer)
    
    def choose_query_menu(self,query_list):
        print("QUERY MENU")
        print("choose query")
        for i in range(0,len(query_list)):
            print(i+1,":",query_list[i])
        answer = input()

        return self.__controller.choose_query_menu(answer)
    
    def insert_row_menu(self,table_name,columns_data):
        print("INSERT MENU")
        print('print data to insert into',table_name)
        answer = {}
        
        for data in columns_data:
            print(data[0],'(',data[1],'):',end=' ')
            inp = input()
            answer.update({data[0] : inp})

        return self.__controller.insert_data(table_name,answer)
    
    def change_row_menu(self,table_name,columns_data):
        print("CHANGE MENU")
        print('print data to change into',table_name)
        answer = {}
        
        for data in columns_data:
            print(data[0],'(',data[1],'):',end=' ')
            inp = input()
            answer.update({data[0] : inp})
        print('WHERE',end =' ')
        inp = input()
        answer.update({'condition' : inp})

        return self.__controller.change_data(table_name,answer)

    def delete_row_menu(self,table_name,column_arr):
        print("DELETE MENU")
        print(table_name)
        print("columns")
        print(column_arr)
        #self.__model.get
        print("WHERE",end = " ")
        answer = input()
        return self.__controller.delete_data(table_name,answer)

    def generate_size_menu(self,table_name):
        print("GENERATE MENU")
        print('print how many rows you want to generate')
        answer = input()
        return self.__controller.generate_data(table_name,answer)

    def cond_query_menu(self,query_num):
        print("QUERY MENU")
        print("WHERE",end = " ")
        cond = input()
        return self.__controller.cond_query_menu(query_num,cond)


