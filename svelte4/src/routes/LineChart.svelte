<script>
    import chartjs from "chart.js/auto";
    import { beforeUpdate, onMount } from "svelte";

    export let tempData;
    export let priceData;
    let chartCanvas;
    let chart;
    $: console.log("pricedata", priceData);
    function drawCanvas() {
        if (tempData) {
            console.log("tempData", tempData);
            let labels = tempData.map((value) => {
                let startTime = new Date(value.startTime);
                return `${startTime.getHours().toString().padStart(2, "0")}:00`;
            });
            let myData = tempData.map((value) => value.value);
            if (chart) chart.destroy();
            let ctx = chartCanvas.getContext("2d");
            chart = new chartjs(ctx, {
                type: "line",
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: "Lämpötila Oulussa",
                            data: myData,
                            backgroundColor: "rgba(0, 255, 255, 1)",
                            borderColor: "rgba(0, 255, 255, 1)",
                            borderWidth: 1,
                            lineTension: 0.2,
                        },
                    ],
                },
            });
        }
        if (priceData) {
            console.log("priceData", priceData);
            let currentDate = null;
            let labels = priceData.map((value) => {
                let parts = value.time.split(" ");
                let date = parts[0];
                let time = parts[1];

                let label = "";
                if (date !== currentDate) {
                    label = date + " " + time;
                    currentDate = date;
                } else {
                    label = time;
                }

                return label;
            });

            let myData = priceData.map((value) => value.price);
            if (chart) chart.destroy();
            let ctx = chartCanvas.getContext("2d");
            chart = new chartjs(ctx, {
                type: "line",
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: "Sähkön hinta c/kWh",
                            data: myData,
                            backgroundColor: "rgba(218, 165, 32, 1)",
                            borderColor: "rgba(0, 0, 0, 1)",
                            borderWidth: 1,
                            lineTension: 0.2,
                        },
                    ],
                },
            });
        }
    }
    onMount(drawCanvas);
    beforeUpdate(drawCanvas);
</script>

<div>
    <canvas bind:this={chartCanvas} />
</div>

<style>
    div {
        border-collapse: collapse;
        background-color: sandybrown;
        box-shadow: 0 0 10px 10px sandybrown;

        width: 70rem;
        height: 50vh;

        margin-bottom: 5rem;
    }
</style>
