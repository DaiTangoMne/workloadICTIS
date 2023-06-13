def start():
    import modify
    import parser.parserExcel as pE

    # modify.insert_educators(pE.get_educators(input("Enter PATH: ")))
    modify.insert_educators(pE.get_df(r'C:\Users\mksim\Desktop\Работа\Нагрузка ИКТИБ\Преподаватели.xlsx'))
    # df = pE.get_df(r'C:\Users\mksim\Desktop\Работа\Нагрузка ИКТИБ\Входной файл.xlsx')
    # modify.insert_entry(df)
    # modify.test_insert()


if __name__ == '__main__':
    start()
