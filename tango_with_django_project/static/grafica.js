
function Visualiza_datos(datos){
        $('#container').highcharts({
            chart: { type: 'bar', animation:'true' },
            title: { text: 'Visitas de los bares' },
            xAxis: { categories: datos[0] },
            //xAxis: {categories: ["Almendro", "mariapilar bar", "Ecu", "Conchita", "Entre ascuas", "Casa Blanca"]},
            yAxis: {
                title:{
                    text:'Visitas'
                }
            },
            series: [{
                data: datos[1],
                name:"numero de visitas",
                //data : [74, 20, 9, 6, 3, 2]
            }],
        });
    };
