homework = "Количество выполненных ДЗ"
homeworkValue = 12

time ='Количество затраченных часов'
timeValue = 1.5


course_name = 'Курс:'
name = 'Python'

time2 = 'Время на одно задание'
timeValue2 = timeValue / homeworkValue

print(course_name, name, ', ' 'всего задач:',homeworkValue,',','затрачено часов:', timeValue,',',
      'среднее время выполнения', timeValue2 )

