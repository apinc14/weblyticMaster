function createBarChart(data, options, targetElementId) {
    var chart = new ApexCharts(document.querySelector(`#${targetElementId}`), {
      chart: {
        type: 'bar',
      },
      series: [
        {
          name: 'Sales',
          data: data,
        },
      ],
      xaxis: {
        categories: options.categories,
      },
    });
    // Render the chart
    chart.render();
  }