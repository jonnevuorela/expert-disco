<script>
    import chartjs from "chart.js/auto";
    import { beforeUpdate } from "svelte";
    export let prodData;
    export let consData;
    let chartCanvas;
    let chart;

    function drawCanvas(prodData, consData) {
        if (prodData && consData) {
            let labels = prodData.map((value) => {
                let startTime = new Date(value.startTime);
                return `${startTime.getHours().toString().padStart(2, "0")}:00`;
            });
            let prodValues = prodData.map((value) => value.value);
            let consValues = consData.map((value) => value.value);
            if (chart) chart.destroy();
            let ctx = chartCanvas.getContext("2d");
            chart = new chartjs(ctx, {
                type: "bar",
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: "Production in MWh/h",
                            data: prodValues,
                            backgroundColor: "rgba(218, 165, 32, 1)",
                            borderColor: "rgba(0, 0, 0, 1)",
                            borderWidth: 1,
                        },
                        {
                            label: "Consumption in MWh/h",
                            data: consValues,
                            backgroundColor: "rgba(244, 164, 96, 1)",
                            borderColor: "rgba(0, 0, 0, 1)",
                            borderWidth: 1,
                        },
                    ],
                },
            });
        }
    }

    beforeUpdate(() => {
        if (
            (prodData && prodData.length > 0) ||
            (consData && consData.length > 0)
        ) {
            drawCanvas(prodData, consData);
        }
    });
</script>

{#if prodData && consData}
    <h3>Production and Consumption</h3>
{/if}
<div>
    <canvas bind:this={chartCanvas} />
</div>

<style>
    div {
        width: 70rem;
        margin-bottom: 5rem;
    }
</style>
