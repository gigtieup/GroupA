const startButton = document.getElementById('start-btn' )
const nextButton = document.getElementById('next-btn' )

const questionContainerElement = document.getElementById (' question-database')
const questionElement = document.getElementById (' question')
const answerButtonsElement=document.getElenentbyId('answer-buttons')


let shuffleQuestions,currectQuestionIndex;
let quizResult =0;






const questions =[
    {
    question: 'What is your preferred risk to reward ratio',
    answer :[
        { text: 'High'}
        {text: 'Low'}
    ]
    },
    {
        question: 'Do you prefer short or long term trades?',
        answer :[
            { text: 'Long'}
            {text: 'Short'}
        ]
        }
]