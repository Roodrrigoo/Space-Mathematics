$(document).ready(function () {

    window.Apex = {
      chart: {
        foreColor: '#ccc',
      },
      stroke: {
        width: 3
      },
      dataLabels: {
        enabled: false
      },
      tooltip: {
        theme: 'dark'
      },
      grid: {
        borderColor: "#535A6C",
        xaxis: {
          lines: {
            show: true
          }
        }
      }
    };
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/puntajeMaximoNiveles",
      method: "GET",
      success: function (data) {
        var puntajeMaximoNivel1 = data.puntaje_maximo_nivel_1[0][1];
        var puntajeMaximoNivel2 = data.puntaje_maximo_nivel_2[0][1];
        var puntajeMaximoNivel3 = data.puntaje_maximo_nivel_3[0][1];
  
        var nombreNivel1 = data.puntaje_maximo_nivel_1[0][0];
        var nombreNivel2 = data.puntaje_maximo_nivel_2[0][0];
        var nombreNivel3 = data.puntaje_maximo_nivel_3[0][0];
  
        var optionDonut = {
          chart: {
            type: 'donut',
            width: '100%',
            height: 200
          },
          dataLabels: {
            enabled: false,//Porcentaje que representa del gráfico
          },
          plotOptions: {
            pie: {
              customScale: 1.1,
              donut: {
                size: '50%',
              },
              offsetY: 0,
            },
            stroke: {
              width: 0,
            }
          },
          colors: ['#00D8B6', '#FF4560', '#775DD0'],
          title: {
            text: 'Puntaje máximo por nivel',
            style: {
              fontSize: '20px',
              color: 'white'
            }
          },
          series: [puntajeMaximoNivel1, puntajeMaximoNivel2, puntajeMaximoNivel3],
          labels: ['Nivel 1 - ' + nombreNivel1, 'Nivel 2 - ' + nombreNivel2, 'Nivel 3 - ' + nombreNivel3],
          legend: {
            position: 'left',
            offsetY: 50,
          }
        };
  
        var donut = new ApexCharts(
          document.querySelector("#donut"),
          optionDonut
        );
        donut.render();
  
      }
    });
  
  
  
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/progresoPromedio",
      method: "GET",
      success: function (data) {
        var progresoPromedio = data;
  
        var optionsProgress = {
          chart: {
            height: 70,
            type: 'bar',
            stacked: true,
            sparkline: {
              enabled: true
            }
          },
          plotOptions: {
            bar: {
              horizontal: true,
              barHeight: '20%',
              colors: {
                backgroundBarColors: ['#40475D']
              },
            },
          },
          stroke: {
            width: 0,
          },
          series: [{
            name: 'Process 1',
            data: [progresoPromedio] //Llenado de la barra
          }],
          title: { //Titulo de la barra
            floating: true,
            offsetX: -10,
            offsetY: 5,
            text: 'Progreso',
            style: {
              color: 'white'
            }
          },
          subtitle: { //El numero de porcentaje
            floating: true,
            align: 'right',
            offsetY: 0,
            text: progresoPromedio + '%',
            style: {
              fontSize: '20px',
              color: 'white',
            }
          },
          tooltip: {
            enabled: false
          },
          xaxis: {
            categories: ['Progreso'],
          },
          yaxis: {
            max: 100 //Maximo de la barra osea 100%
          },
          fill: {
            type: 'gradient',
            gradient: {
              shade: 'light',
              type: 'horizontal',
              shadeIntensity: 0.5,
              gradientToColors: ['#388E3C', '#4CAF50', '#4CAF50']
            }
          }
        };
  
        var chartProgress = new ApexCharts(document.querySelector('#progreso'), optionsProgress);
        chartProgress.render();
  
      }
    });
  
  
  
  
  
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/topGlobal",
      method: "GET",
      success: function (data) {
        var nombres = [];
        var puntajes = []
  
        for (var i = 0; i < data.length; i++) {
          nombres.push(data[i][0]);
          puntajes.push(data[i][1]);
        }
  
        var optionsColumn = {
          chart: {
            type: 'bar',
            height: 350,
            toolbar: {
              show: true
            },
            zoom: {
              enabled: true
            }
          },
          series: [{
            name: 'Puntaje Obtenido',
            data: puntajes
          }],
          plotOptions: {
            bar: {
              horizontal: false,
              borderRadius: 5
            }
          },
          dataLabels: {
            enabled: false
          },
          stroke: {
            width: 0
          },
          title: {
            text: 'Top 5 Global',
            align: 'left',
            style: {
              fontSize: '20px',
              color: 'white'
            }
          },
          fill: {
            type: 'gradient',
            gradient: {
              shade: 'dark',
              type: 'vertical',
              shadeIntensity: 0.5,
              inverseColors: false,
              opacityFrom: 1,
              opacityTo: 0.8,
              stops: [0, 100],
              colorStops: [
                {
                  offset: 0,
                  color: '#F55555'
                },
                {
                  offset: 100,
                  color: '#6078ea'
                }
              ]
            }
          },
          xaxis: {
            categories: nombres
          },
          legend: {
            show: true
          },
          responsive: [{
            breakpoint: 480,
            options: {
              legend: {
                position: 'bottom',
                offsetX: -10,
                offsetY: 0
              }
            }
          }]
        };
  
        var chartColumn = new ApexCharts(
          document.querySelector("#columnchart"),
          optionsColumn
        );
        chartColumn.render();
      }
    });
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/topM",
      method: "GET",
      success: function (data) {
        var nombres = [];
        var puntajes = []
  
        for (var i = 0; i < data.length; i++) {
          nombres.push(data[i][0]);
          puntajes.push(data[i][1]);
        }
  
        var optionsColumn = {
          chart: {
            type: 'bar',
            height: 350,
            toolbar: {
              show: true
            },
            zoom: {
              enabled: true
            }
          },
          series: [{
            name: 'Puntaje Obtenido',
            data: puntajes
          }],
          plotOptions: {
            bar: {
              horizontal: false, //Si sale vertical o horizontal
              borderRadius: 5
            }
          },
          dataLabels: {
            enabled: false //Mostrar numeros dentro de la columna
          },
          stroke: {
            width: 0 //Contorno de las barras
          },
          title: {
            text: 'Top 5 Niños',
            align: 'left',
            style: {
              fontSize: '20px',
              color: 'white'
            }
          },
          fill: {
            type: 'gradient',
            gradient: {
              shade: 'dark',
              type: 'vertical',
              shadeIntensity: 0.5,
              inverseColors: false,
              opacityFrom: 1,
              opacityTo: 0.8,
              stops: [0, 100],
              colorStops: [
                {
                  offset: 0, // Posición del primer color (0-100)
                  color: '#F55555' // Primer color del gradiente
                },
                {
                  offset: 100, // Posición del segundo color (0-100)
                  color: '#6078ea' // Segundo color del gradiente
                }
              ]
            }
          },
          xaxis: {
            categories: nombres
          },
          legend: {
            show: true
          },
          responsive: [{
            breakpoint: 480,
            options: {
              legend: {
                position: 'bottom',
                offsetX: -10,
                offsetY: 0
              }
            }
          }]
        };
  
        var chartColumn = new ApexCharts(
          document.querySelector("#topniños"),
          optionsColumn
        );
        chartColumn.render();
      }
    });
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/topF",
      method: "GET",
      success: function (data) {
        var nombres = [];
        var puntajes = []
  
        for (var i = 0; i < data.length; i++) {
          nombres.push(data[i][0]);
          puntajes.push(data[i][1]);
        }
  
        var optionsColumn = {
          chart: {
            type: 'bar',
            height: 350,
            toolbar: {
              show: true
            },
            zoom: {
              enabled: true
            }
          },
          series: [{
            name: 'Puntaje Obtenido',
            data: puntajes
          }],
          plotOptions: {
            bar: {
              horizontal: false, //Si sale vertical o horizontal
              borderRadius: 5
            }
          },
          dataLabels: {
            enabled: false //Mostrar números dentro de la columna
          },
          stroke: {
            width: 0 //Contorno de las barras
          },
          title: {
            text: 'Top 5 Niñas',
            align: 'left',
            style: {
              fontSize: '20px',
              color: 'white'
            }
          },
          fill: {
            type: 'gradient',
            gradient: {
              shade: 'dark',
              type: 'vertical',
              shadeIntensity: 0.5,
              inverseColors: false,
              opacityFrom: 1,
              opacityTo: 0.8,
              stops: [0, 100],
              colorStops: [
                {
                  offset: 0, // Posición del primer color (0-100)
                  color: '#F55555' // Primer color del gradiente
                },
                {
                  offset: 100, // Posición del segundo color (0-100)
                  color: '#6078ea' // Segundo color del gradiente
                }
              ]
            }
          },
          xaxis: {
            categories: nombres
          },
          legend: {
            show: true
          },
          responsive: [{
            breakpoint: 480,
            options: {
              legend: {
                position: 'bottom',
                offsetX: -10,
                offsetY: 0
              }
            }
          }]
        };
  
        var chartColumn = new ApexCharts(
          document.querySelector("#topniñas"),
          optionsColumn
        );
        chartColumn.render();
      }
    });
  
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/peoresGlobal",
      method: "GET",
      success: function (data) {
        var nombres = [];
        var puntajes = []
  
        for (var i = 0; i < data.length; i++) {
          nombres.push(data[i][0]);
          puntajes.push(data[i][1]);
        }
  
        var optionsColumn = {
          chart: {
            type: 'bar',
            height: 350,
            toolbar: {
              show: true
            },
            zoom: {
              enabled: true
            }
          },
          series: [{
            name: 'Puntaje Obtenido',
            data: puntajes
          }],
          plotOptions: {
            bar: {
              horizontal: true, //Si sale vertical o horizontal
              borderRadius: 5
            }
          },
          dataLabels: {
            enabled: false //Mostrar numeros dentro de la columna
          },
          stroke: {
            width: 0 //Contorno de las barras
          },
          title: {
            text: 'Peores Global',
            align: 'left',
            style: {
              fontSize: '20px',
              color: 'white'
            }
          },
          fill: {
            type: 'gradient',
            gradient: {
              shade: 'dark',
              type: 'vertical',
              shadeIntensity: 0.5,
              inverseColors: false,
              opacityFrom: 1,
              opacityTo: 0.8,
              stops: [0, 100],
              colorStops: [
                {
                  offset: 0, // Posición del primer color (0-100)
                  color: '#F55555' // Primer color del gradiente
                },
                {
                  offset: 100, // Posición del segundo color (0-100)
                  color: '#6078ea' // Segundo color del gradiente
                }
              ]
            }
          },
          xaxis: {
            categories: nombres
          },
          legend: {
            show: true
          },
          responsive: [{
            breakpoint: 480,
            options: {
              legend: {
                position: 'bottom',
                offsetX: -10,
                offsetY: 0
              }
            }
          }]
        };
  
        var chartColumn = new ApexCharts(
          document.querySelector("#peores"),
          optionsColumn
        );
        chartColumn.render();
      }
    });
  
  
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/peoresM",
      method: "GET",
      success: function (data) {
        var nombres = [];
        var puntajes = []
  
        for (var i = 0; i < data.length; i++) {
          nombres.push(data[i][0]);
          puntajes.push(data[i][1]);
        }
  
        var optionsColumn = {
          chart: {
            type: 'bar',
            height: 350,
            toolbar: {
              show: true
            },
            zoom: {
              enabled: true
            }
          },
          series: [{
            name: 'Puntaje Obtenido',
            data: puntajes
          }],
          plotOptions: {
            bar: {
              horizontal: true, //Si sale vertical o horizontal
              borderRadius: 5
            }
          },
          dataLabels: {
            enabled: false //Mostrar numeros dentro de la columna
          },
          stroke: {
            width: 0 //Contorno de las barras
          },
          title: {
            text: 'Peores Niños',
            align: 'left',
            style: {
              fontSize: '20px',
              color: 'white'
            }
          },
          fill: {
            type: 'gradient',
            gradient: {
              shade: 'dark',
              type: 'vertical',
              shadeIntensity: 0.5,
              inverseColors: false,
              opacityFrom: 1,
              opacityTo: 0.8,
              stops: [0, 100],
              colorStops: [
                {
                  offset: 0, // Posición del primer color (0-100)
                  color: '#F55555' // Primer color del gradiente
                },
                {
                  offset: 100, // Posición del segundo color (0-100)
                  color: '#6078ea' // Segundo color del gradiente
                }
              ]
            }
          },
          xaxis: {
            categories: nombres
          },
          legend: {
            show: true
          },
          responsive: [{
            breakpoint: 480,
            options: {
              legend: {
                position: 'bottom',
                offsetX: -10,
                offsetY: 0
              }
            }
          }]
        };
  
        var chartColumn = new ApexCharts(
          document.querySelector("#peoresniños"),
          optionsColumn
        );
        chartColumn.render();
      }
    });
  
  
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/peoresF",
      method: "GET",
      success: function (data) {
        var nombres = [];
        var puntajes = []
  
        for (var i = 0; i < data.length; i++) {
          nombres.push(data[i][0]);
          puntajes.push(data[i][1]);
        }
  
        var optionsColumn = {
          chart: {
            type: 'bar',
            height: 350,
            toolbar: {
              show: true
            },
            zoom: {
              enabled: true
            }
          },
          series: [{
            name: 'Puntaje Obtenido',
            data: puntajes
          }],
          plotOptions: {
            bar: {
              horizontal: true, //Si sale vertical o horizontal
              borderRadius: 5
            }
          },
          dataLabels: {
            enabled: false //Mostrar numeros dentro de la columna
          },
          stroke: {
            width: 0 //Contorno de las barras
          },
          title: {
            text: 'Peores Niñas',
            align: 'left',
            style: {
              fontSize: '20px',
              color: 'white'
            }
          },
          fill: {
            type: 'gradient',
            gradient: {
              shade: 'dark',
              type: 'vertical',
              shadeIntensity: 0.5,
              inverseColors: false,
              opacityFrom: 1,
              opacityTo: 0.8,
              stops: [0, 100],
              colorStops: [
                {
                  offset: 0, // Posición del primer color (0-100)
                  color: '#F55555' // Primer color del gradiente
                },
                {
                  offset: 100, // Posición del segundo color (0-100)
                  color: '#6078ea' // Segundo color del gradiente
                }
              ]
            }
          },
          xaxis: {
            categories: nombres
          },
          legend: {
            show: true
          },
          responsive: [{
            breakpoint: 480,
            options: {
              legend: {
                position: 'bottom',
                offsetX: -10,
                offsetY: 0
              }
            }
          }]
        };
  
        var chartColumn = new ApexCharts(
          document.querySelector("#peoresniñas"),
          optionsColumn
        );
        chartColumn.render();
      }
    });
  
  
  
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/exito_fallo",
      method: "GET",
      success: function (data) {
        var porcentajeExito = data["Nivel 1"]["exito"];
        var porcentajeFallo = data["Nivel 1"]["fallo"];
  
        var pie1 = {
          title: {
            text: 'Porcentaje de Éxito/Fallo 1° Nivel',
            align: 'left',
            style: {
              fontSize: '18px',
              color: 'white',
            }
          },
          series: [porcentajeExito, porcentajeFallo],
          chart: {
            width: 380,
            type: 'pie',
          },
          plotOptions: {
            pie: {
              dataLabels: {
                enabled: true,
                formatter: function (val, opts) {
                  return opts.seriesIndex === 0 ? 'Éxito: ' + val : 'Fallo: ' + val;
                }
              },
              startAngle: -180,
              endAngle: 180,
            }
          },
          colors: ['#00D8B6', '#FF4560'],
          tooltip: {
            enabled: true,
            y: {
              formatter: function (value, { seriesIndex }) {
                var total = pie1.series.reduce((a, b) => a + b, 0);
                var percentage = ((value / total) * 100).toFixed(2);
                return percentage + '%';
              }
            }
          },
          labels: ['Éxito', 'Fallo'],
          legend: {
            position: 'right',
            offsetY: 100,
          }
  
        };
  
  
        var chart = new ApexCharts(document.querySelector("#exito_fallo_1"), pie1);
        chart.render();
  
      }
    });
  
  
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/exito_fallo",
      method: "GET",
      success: function (data) {
        var porcentajeExito = data["Nivel 2"]["exito"];
        var porcentajeFallo = data["Nivel 2"]["fallo"];
  
        var pie2 = {
          title: {
            text: 'Porcentaje de Éxito/Fallo 2° Nivel',
            align: 'left',
            style: {
              fontSize: '18px',
              color: 'white',
            }
          },
          series: [porcentajeExito, porcentajeFallo],
          chart: {
            width: 380,
            type: 'pie',
          },
          plotOptions: {
            pie: {
              dataLabels: {
                enabled: true,
                formatter: function (val, opts) {
                  return opts.seriesIndex === 0 ? 'Éxito: ' + val : 'Fallo: ' + val;
                }
              },
              startAngle: -180,
              endAngle: 180,
            }
          },
          colors: ['#00D8B6', '#FF4560'],
          tooltip: {
            enabled: true,
            y: {
              formatter: function (value, { seriesIndex }) {
                var total = pie2.series.reduce((a, b) => a + b, 0);
                var percentage = ((value / total) * 100).toFixed(2);
                return percentage + '%';
              }
            }
          },
          labels: ['Éxito', 'Fallo'],
          legend: {
            position: 'right',
            offsetY: 100,
          }
  
        };
  
  
        var chart = new ApexCharts(document.querySelector("#exito_fallo_2"), pie2);
        chart.render();
  
      }
    });
  
  
  
    $.ajax({
      url: "https://rodr1g0fernand0.pythonanywhere.com/exito_fallo",
      method: "GET",
      success: function (data) {
        var porcentajeExito = data["Nivel 3"]["exito"];
        var porcentajeFallo = data["Nivel 3"]["fallo"];
  
        var pie3 = {
          title: {
            text: 'Porcentaje de Éxito/Fallo 3° Nivel',
            align: 'left',
            style: {
              fontSize: '18px',
              color: 'white',
            }
          },
          series: [porcentajeExito, porcentajeFallo],
          chart: {
            width: 380,
            type: 'pie',
          },
          plotOptions: {
            pie: {
              dataLabels: {
                enabled: true,
                formatter: function (val, opts) {
                  return opts.seriesIndex === 0 ? 'Éxito: ' + val : 'Fallo: ' + val;
                }
              },
              startAngle: -180,
              endAngle: 180,
            }
          },
          colors: ['#00D8B6', '#FF4560'],
          tooltip: {
            enabled: true,
            y: {
              formatter: function (value, { seriesIndex }) {
                var total = pie3.series.reduce((a, b) => a + b, 0);
                var percentage = ((value / total) * 100).toFixed(2);
                return percentage + '%';
              }
            }
          },
          labels: ['Éxito', 'Fallo'],
          legend: {
            position: 'right',
            offsetY: 100,
          }
  
        };
  
  
        var chart = new ApexCharts(document.querySelector("#exito_fallo_3"), pie3);
        chart.render();
  
      }
    });
  
    chartArea.render();
  
  });