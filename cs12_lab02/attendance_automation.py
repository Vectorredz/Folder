def attendance_summary(enrolment_list: list[tuple], attendance_sheet: list[str]):
    '''
    strings = list(map(str, str(attendance_sheet[i] for i in range(len(attendance_sheet))).split()))
    new = [''.join(i.upper().replace(',', '').split()) for i in strings]
    return new
    '''
    symbs = "1234567890!@#$%^&*()_+|}{?/|.,></~`"
    count = 0
    new: list[tuple[None]] = []
    attendance: dict[str, list[str]] = {'present': [], 'absent': []}
    for i in attendance_sheet:
        print(i)
            

    '''
    if name_tuple in enrolment_list:
        attendance['present'].append(name_tuple)
    else:
        attendance['absent'].append(name_tuple)
    '''

    


print(attendance_summary([
 ('JUAN', 'OBZUNAR'), ('ETHAN', 'MISLANG')]
, ['Juan, Obzunar    ', 'ethaN, Mislang', 'antony']))