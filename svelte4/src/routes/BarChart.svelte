<script>
    import chartjs from "chart.js/auto";
    import { beforeUpdate } from "svelte";
    export let data;
    let chartCanvas;
    let labels = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
    ];
    let chart;
    function drawCanvas() {
        if (data) {
            let myData = data.map((value) => value.value);
            if (chart) chart.destroy();
            let ctx = chartCanvas.getContext("2d");
            chart = new chartjs(ctx, {
                type: "bar",
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: "Production in MWh/h",
                            data: myData,
                        },
                    ],
                },
            });
        }
    }
    beforeUpdate(drawCanvas);
</script>

<div>
    <canvas bind:this={chartCanvas} />
</div>

<style>
    div {
        width: 75vw;
    }
</style>
