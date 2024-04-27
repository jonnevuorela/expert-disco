<script>
    import LineChart from "./LineChart.svelte";

    let startDate;
    let endDate;
    let button = false;
    let data;
    let priceData;
    $: priceData = data;
    $: if (button) doGetRequest();
    async function doGetRequest() {
        fetch(
            `http://localhost:5000/testi?startDate=${startDate}&endDate=${endDate}`,
            {
                method: "GET",
            },
        )
            .then((response) => {
                if (!response.ok) {
                    throw new Error("HTTP error" + response.status);
                }
                return response.text();
            })
            .then((json) => {
                if (!json) {
                    console.log("No data");
                    return;
                } else {
                    json = JSON.parse(json);
                    data = json.Publication_MarketDocument.TimeSeries.map(
                        (series) => {
                            return series.Period.Point.map((point, index) => {
                                let price = point.price / 10;
                                let hour = point.position - 1;
                                let day = new Date(
                                    series.Period.timeInterval.start,
                                ).getDate();
                                let month =
                                    new Date(
                                        series.Period.timeInterval.start,
                                    ).getMonth() + 1;
                                let time =
                                    day + "." + month + " " + hour + ":00";

                                console.log(time);

                                return {
                                    time: time,
                                    price: price,
                                };
                            });
                        },
                    ).flat();
                }
            });
    }
</script>

<h1>Get electricity prices for certain date</h1>
<p>
    Choose the start date
    <input type="date" bind:value={startDate} />
</p>
<p>
    Choose the end date
    <input type="date" bind:value={endDate} />
</p>
<button style="margin-bottom: 3rem;" on:click={doGetRequest}>Get prices</button>
<LineChart {priceData} />
