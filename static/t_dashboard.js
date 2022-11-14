function goBackT_Dashboard(){
    window.location.href = ('http://127.0.0.1:5000/t_dashboard')
}

$(".grade").each((_, el) => {
    $(el).on('change', () => {
       $(el).addClass("changed")
    })
})

function updateGrades() {

    $(".changed").each((e, el) => {
        console.log("Name: ", $(el).attr('id'))
        console.log("Grade: ", $(el).val())

        const updateGrade = {
            userId: $(el).attr('id'),
            newGrade:$(el).val()
        }

        fetch('http://127.0.0.1:5000/updateGrade', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(updateGrade)
            })
            .then(() => {
                console.log('successful')
            })
            .catch((response) => {
                console.log('update for ' + updateGrade['userId'] + ' was unsuccessfull')
            })

        console.log(updateGrade)
    })

}