def attendance_summary(enrolment_list: list[tuple[str, str]], attendance_sheet: list[str]) -> dict[str, list[tuple[str]] | int]:
    attendance: dict[str, list[tuple[str]] | int] = {'present': [], 'absent': [], 'ill-formed': 0}
    enrolment_set: list[list[str]] = [sorted(item) for item in enrolment_list]  
    for i in range(len(attendance_sheet)):
        name = str(attendance_sheet[i]).upper().strip().split(',')
        name_set = sorted([n.strip() for n in name])  
        if name_set in enrolment_set and name_set not in attendance['present']:
            attendance['present'].append(tuple(name_set))
            enrolment_set.remove(name_set)
        else:
            attendance['ill-formed'] += 1
    attendance['absent'] = enrolment_set
    return attendance


print(attendance_summary([
 ('JUAN', 'OBZUNAR'),
 ('KELLY', 'MAYUYU'),
 ('ALEJANDRO', 'PAU'),
 ('JUSTIN', 'BUGAOAN'),
 ('RAINER', 'REBOLLIDO'),
 ('GABRIEL', 'MISLANG'),
 ('JUAN CHO', 'CORONEL'),
 ('JUAN', 'CHO CORONEL'),
], [
 'Coronel, Juan Cho',
 'Coronel Juan , Cho ',
 'Coronel, JuanCho',
 'Coronel Juan Cho',
 'Coronel,\nJuan\tCho',
 'Coronel, Juan, Cho',
 'REBOLLIDO RAINER',
 'PAU,Alejandr ',
 'BUGA0AN, JUSTIN',
 'Juan, Obzunar',
 ' Mayuyu , KELLY ',
 'pau,\nalejandro ',
 'Mislang, Juan ',
 'Beltran, JEroMe',
 ' \t\n ^_^ n/t/ ',
 'Obzunar,\\Juan',
]))



'''We will consider a entry in the attendance sheet well-formed if it is of the intended form [STUDENT], [GIVEN NAME] for some student (after being
lenient in the above way), and in that case, that student will be considered present. Any student not identified present after processing all entries
of the attendance sheet will be considered absent. And if the names in the attendance sheets are not well-formed need to count ill-formed'''