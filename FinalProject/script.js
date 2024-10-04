
// for the quiz check the answers
function check(){

    var output = document.getElementById("output");
    var question1 = document.quiz.question1.value;
    var question2 = document.quiz.question2.value;
    var question3 = document.quiz.question3.value;
    var question4 = document.quiz.question4.value;
    var question5 = document.quiz.question5.value;
    var question6 = document.quiz.question6.value;
    var question7 = document.quiz.question7.value;
    var question8 = document.quiz.question8.value;
    var question9 = document.quiz.question9.value;
    var question10 = document.quiz.question10.value;
    var correct = 0;

    if(question1 == "Instagram"){
        correct++;
    }

    if(question2 == "Jupiter"){
        correct++;
    }

    if(question3 == "7"){
        correct++
    }

    if(question4 == "4kg"){
        correct++;
    }

    if(question5 == "Germany"){
        correct++;
    }

    if(question6 == "Greenland"){
        correct++;
    }

    if(question7 == "Antarctica"){
        correct++;
    }

    if(question8 == "Carbon dioxide"){
        correct++;
    }

    if(question9 == "Earthquakes"){
        correct++;
    }

    if(question10 == "Morocco"){
        correct++;
    }

    let incorrect = document.getElementsByName("incorrect");
    for(let i = 0; i < incorrect.length; i++){
        incorrect[i].style.color = "red";
    }

    let correctt = document.getElementsByName("correct");
    for(let j = 0; j < correctt.length; j++){
        correctt[j].style.color = "green";
    }


    output.className = "shown";
    output.innerHTML = " Result: You got " + correct + " answers correct";


};


function noscroll(){
    bodyquiz = document.getElementById("bodyquiz");

    window.addEventListener("load", function(){
        bodyquiz.classList.remove('noscroll');
    })


}



// to upload image and display it
const image_input = document.querySelector("#image_input");
        var uploaded_image = "";

        image_input.addEventListener("change", function(){
        const reader = new FileReader();
        reader.addEventListener("load", () => {
            uploaded_image = reader.result;
            document.querySelector("#display_image").style.backgroundImage = `url(${ uploaded_image})`  ;
        });

        reader.readAsDataURL(this.files[0]);
    });
