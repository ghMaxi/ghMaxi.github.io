function dt()
{
    let data = [[["сентябрь", 10, "Тест", "about:blank"],
                 ["октябрь",  11, "Сем.", "about:blank",
                              21, "Тест", "about:blank"]],
                [["Студент студентский", 4, 4, 5,],
                 ["Студентка студентская", 5, 3, 5]]]

    let calendar = Array(data[0].length)
    this.calendar = calendar
    let students = Array(data[1].length)
    this.students = students

    for (let i = 0; i < calendar.length; i++)
    {
        let events = Array((data[0][i].length - 1) / 3)
        calendar[i] = {month: data[0][i][0], events: events}
        for (let j = 0; j < events.length; j++)
        {
            let k = j * 3 + 1
            events[j] = {day: data[0][i][k], type: data[0][i][k+1], url: data[0][i][k+2]}
        }
    }

    for (let i = 0; i < students.length; i++)
    {
        let marks = Array(data[1][i].length - 1)
        students[i] = {name: data[1][i][0], marks: marks}
        for (let j = 0; j < marks.length; j++)
            marks[j] = data[1][i][j + 1]
    }
}
