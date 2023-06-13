/*fetch("http://localhost:8000/api/v1/sensores/piscina=1")
.then(response => response.json())
.then(data=> {
    var ctx = document.getElementById('miGrafica').getContext('2d');
    var chart = new Chart(ctx,{
        type:'bar',
    }) 
    // Crear una barra de progreso para cada dato sensor
   for (var i = 0; i < data.length; i++) {
    var sensor = data[i];
    var label = sensor.tipo;
    var percentage = sensor.rango;

    var progressBar = createProgressBar(label, percentage);
    progressContainer.appendChild(progressBar);
  }
})*/
var ctx = document.getElementById('miGrafica').getContext('2d');
var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Turbidez', 'PH', 'Alcalinidad'],
        datasets: [{
            label: 'calidad de agua',
            backgroundColor: '#FF5733',
            borderColor: '#FF5733',
            data: [50, 90, 34]
        }]
    },
    options: {}
});

 // Obtener los datos de la API
 fetch("http://localhost:8000/api/v1/sensores/piscina=1")
 .then(response => response.json())
 .then(data => {
   var progressContainer = document.getElementById("miGrafica");

   // Crear una barra de progreso para cada dato sensor
   for (var i = 0; i < data.length; i++) {
     var sensor = data[i];
     var label = sensor.tipo;
     var percentage = sensor.rango;

     var progressBar = createProgressBar(label, percentage);
     progressContainer.appendChild(progressBar);
   }
 })
 .catch(error => {
   console.error("Error al obtener los datos de la API:", error);
 });