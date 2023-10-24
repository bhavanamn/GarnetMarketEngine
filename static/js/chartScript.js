
document.addEventListener("DOMContentLoaded", function () {
    // Define your chart container element
    const chartContainer = document.getElementById("line-chart");

    // Create a new Lightweight Charts instance
    const chart = LightweightCharts.createChart(chartContainer, {
        width: chartContainer.clientWidth,
        height: chartContainer.clientHeight,
    });

    // Create a new line series
    const series = chart.addLineSeries();

    // Define the data for the chart (you can replace this with your actual data)
    const data = [
        { time: "2023-10-01", value: 100 },
        { time: "2023-10-02", value: 110 },
        { time: "2023-10-03", value: 120 },
        // Add more data points as needed
    ];

    // Apply the data to the line series
    series.setData(data);

    // Adjust the chart layout (optional)
    chart.timeScale().fitContent();
});

