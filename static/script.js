// might need window.location.href = '../'; because render_template not working

function login() {
    
    userName = $('#username').val()
    password =  $('#password').val()

    // if input fields are empty

    if (username == '' || password == '') {
        console.log('input fields not filled')
    } else {
        const loginInput = {
            username: userName,
            password: password
        }

        fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginInput)
        })
        .then((response) => response.json())
        .then((body) => {
            
            //client-side redirection
            window.location.href = body.redirect;
        })
        .catch((response) => {
            console.log('login request was unsuccessful')
        })
    }
}