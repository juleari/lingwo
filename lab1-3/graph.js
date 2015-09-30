(function () {

    var Graph = function(elemName, name, categories, series) {
        console.log(arguments);
        $(elemName).highcharts({
            chart: {
                type: 'line',
                marginRight: 130,
                marginBottom: 25
            },
            title: {
                text: name,
                x: -20 //center
            },
            xAxis: {
                categories: categories
            },
            yAxis: {
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: 0,
                y: 100,
                borderWidth: 0
            },
            series: series
        });
    }

    $.getJSON('/data', function (json) {

        console.log(json);

        var data = [], data2 = [], ser = [], cat = [];

        for (var i = 0; i < 500; i+= 1) {
            cat.push( json[i].name );
            data.push( json[i].data );
            data2.push( json[i].cypf );
        }

        ser.push({name: 'Мастер и Маргарита', data: data});

        Graph('#js-graph', 'График распределения слов в романе Мастер и Маргарита', cat, ser);
        ser = [{name: 'Распределение Ципфа', data: data2}];
        Graph('#js-graph2', 'График распределения Ципфа', cat, ser);
    });

})();