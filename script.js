$(function () {

  $.getJSON( "series.json", function( series ) {

    series[0].color = '#688FE2'
    series[0].color = '#EB6E7B'

    $('#container').highcharts({
      chart: {
        type: 'scatter',
        zoomType: 'xy'
      },
      title: {
        text: 'European Referendum Analysis'
      },
      subtitle: {
        text: '<a href="https://github.com/miskinh/referendum-results">https://github.com/miskinh/referendum-results</a>'
      },
      xAxis: {
        title: {
          text: '% of Votes to Remain in the European Union',
          style: {
            'font-size': '20px'
          }
        }
      },
      yAxis: {
        title: {
          text: '% of People in Area',
          style: {
            'font-size': '20px'
          }
        }
      },
      legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 100,
        y: 70,
        floating: true,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF',
        borderWidth: 1
      },
      tooltip: {
        headerFormat: '',
        pointFormat: '{point.name}'
      },
      plotOptions: {
        scatter: {
          marker: {
            radius: 4,
            states: {
              hover: {
                enabled: true,
                lineColor: 'rgb(100,100,100)'
              }
            }
          },
          states: {
            hover: {
              marker: {
                enabled: false
              }
            }
          }
        }
      },
      series: series
    });


  });

});

