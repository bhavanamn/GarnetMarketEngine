document.addEventListener("DOMContentLoaded", function () {
    // Create a container for the chart
    const chartContainer = document.getElementById("chart-container");

    // Create a new chart
    const chart = LightweightCharts.createChart(chartContainer, {
        width: chartContainer.clientWidth,
        height: chartContainer.clientHeight,
    });

    // Create line series for the data and prediction
    const lineSeries = chart.addLineSeries({ color: 'blue' });
    const predSeries = chart.addLineSeries({ color: 'red' });

    // Fetch data for the "data" series
    fetch('/chart-data')
        .then(response => response.json())
        .then(data => {
            // Set the data for the "data" series
            lineSeries.setData(data);
        });

    // Fetch data for the "prediction" series
    fetch('/pred')
        .then(response => response.json())
        .then(data => {
            // Set the data for the "prediction" series
            predSeries.setData(data);
        });
});
