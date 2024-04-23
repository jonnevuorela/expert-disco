<script>
    import DataTable from "./DataTable.svelte";
    import BarChart from "./BarChart.svelte";

    let data;
    let date_value;

    $: date_value != null ? fetchData(date_value) : null;
    function fetchData(date_value) {
        fetch(`http://localhost:5000/e_production?startTime=${date_value}T00:00:0
    0Z&endTime=${date_value}T23:45:00Z`)
            .then((response) => {
                return response.json();
            })
            .then((result) => {
                data = result.data;
                data = data.map((value) => {
                    // Tässä muutetaan startTime ja endTime tunnit Suomen aikaan ja
                    // samalla tehdään stringistä date tyyppinen objekti, jota on helpompi
                    // käsitellä myöhemmin koodissa
                    let startTime = new Date(value.startTime);
                    startTime.setHours(startTime.getHours() - 3);
                    value.startTime = startTime;
                    let endTime = new Date(value.endTime);
                    endTime.setHours(endTime.getHours() - 3);
                    value.endTime = endTime;
                    return value;
                });
                // Otetaan vain joka neljäs hakutulos, koska näin saadaan yksi
                // hakutulos per tunti, joka on riittävä graafien
                // piirtämistä varten tässä
                data = data.filter((value, index) => index % 4 == 0);
                console.log(data);
            });
    }
</script>

<h1>Electricity production in Finland</h1>
<p>Choose the date <input type="date" bind:value={date_value} /></p>
<DataTable {data} />
<BarChart {data} />
```
