let number = document.querySelectorAll('.number')
let number1 = document.getElementById('number');
let number2 = document.getElementById('number2');
let number3 = document.getElementById('number3');
let number4 = document.getElementById('number4');
let number5 = document.getElementById('number5');
let counter = 0;
let counter1 = 0;
let counter2 = 0;
let counter3 = 0;
let counter4 = 0;


/////For first chart
setInterval(() => {
    if (counter == 65) {
        clearInterval()
    } else {
        counter++;
        number1.innerHTML = counter + '%';
    }
}, 65 / 2)
setInterval(() => {
    if (counter1 == 40) {
        clearInterval()
    } else {
        counter1++;
        number2.innerHTML = counter1 + '%';
    }
}, 40 / 2)
setInterval(() => {
    if (counter2 == 45) {
        clearInterval()
    } else {
        counter2++;
        number3.innerHTML = counter2 + '%';
    }
}, 45 / 2)
setInterval(() => {
    if (counter3 == 70) {
        clearInterval()
    } else {
        counter3++;
        number4.innerHTML = counter3 + '%';
    }
}, 70 / 2)
setInterval(() => {
        if (counter4 == 35) {
            clearInterval()
        } else {
            counter4++;
            number5.innerHTML = counter4 + '%';
        }
    }, 35 / 2)
    //////////////////////////////////////////chart
let chart = document.getElementById('myChart').getContext('2d');
let labels = [];

for (var i = 1; i <= 187; i++) {
    labels.push(i);
}


const data = {
    labels: labels,
    datasets: [{
        label: 'ECG HEART RATE',
        borderColor: '#fff',
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: [0.977941, 0.926471, 0.681373, 0.245098, 0.154412, 0.191176, 0.151961, 0.085784, 0.058824, 0.04902, 0.044118, 0.061275, 0.066176, 0.061275, 0.04902, 0.073529, 0.061275, 0.061275, 0.066176, 0.068627, 0.095588, 0.07598, 0.093137, 0.105392, 0.115196, 0.102941, 0.117647, 0.125, 0.142157, 0.127451, 0.151961, 0.144608, 0.164216, 0.144608, 0.159314, 0.151961, 0.154412, 0.142157, 0.151961, 0.151961, 0.147059, 0.132353, 0.127451, 0.134804, 0.137255, 0.112745, 0.107843, 0.105392, 0.107843, 0.098039, 0.093137, 0.102941, 0.10049, 0.105392, 0.102941, 0.117647, 0.105392, 0.122549, 0.127451, 0.142157, 0.147059, 0.144608, 0.17402, 0.230392, 0.237745, 0.247549, 0.230392, 0.22549, 0.198529, 0.176471, 0.132353, 0.125, 0.117647, 0.122549, 0.112745, 0.129902, 0.115196, 0.083333, 0.0, 0.066176, 0.306373, 0.612745, 0.860294, 1.0, 0.958333, 0.745098, 0.303922, 0.164216, 0.205882, 0.164216, 0.102941, 0.095588, 0.090686, 0.10049, 0.095588, 0.098039, 0.093137, 0.098039, 0.095588, 0.112745, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    }]
};

const config = {
    type: 'line',
    data: data,
    options: {
        responsive: true,
        radius: 1,
    }
};
const myChart = new Chart(chart, config);

///////////////////////////////active link
let links = document.querySelectorAll('.nav-link')


links.forEach(link => {
    link.addEventListener('click', () => {
        links.forEach(link => {
            link.classList.remove('active')
        })
        link.classList.add('active')
    })
})