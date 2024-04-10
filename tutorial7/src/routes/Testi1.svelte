<script>
    import { onMount } from "svelte";
    const url = "https://rata.digitraffic.fi/api/v2/graphql/graphql";
    let trains;
    //$: console.log(trains)
    function fetchData() {
        const q1 = {
            query: `{
              currentlyRunningTrains(where: {operator: {shortCode: {equals: "vr"}}}) {
                operator {
                  shortCode
                }
                trainNumber
                departureDate
                trainLocations(
                  where: {speed: {greaterThan: 30}}
                  orderBy: {timestamp: DESCENDING}
                  take: 1
                ) {
                  speed
                  timestamp
                  location
                }
              }
            }`,
        };
        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept-Encoding": "gzip",
            },
            body: JSON.stringify(q1),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then((result) => {
                trains = result.data.currentlyRunningTrains;
                console.log(trains);
                trains = trains.map((value) => {
                    if (value.trainLocations) {
                        let timestamp = value.trainLocations[0].timestamp;
                        value.trainLocations[0].timestamp = new Date(timestamp);
                        return value;
                    } else {
                        return null;
                    }
                });
                trains = trains.filter((value) => value != null);
            });
    }
    onMount(fetchData);
</script>

{#if trains && trains.length > 0}
    <table>
        <tr>
            <th>Train number</th>
            <th>DepartureDate</th>
            <th>Time</th>
            <th>Location</th>
        </tr>
        {#each trains as train}
            <tr>
                <td>{train.trainNumber}</td>
                <td>{train.departureDate}</td>
                {#if train.trainLocations}
                    <td
                        >{train.trainLocations[0].timestamp.getHours()}:{train.trainLocations[0].timestamp.getMinutes()}</td
                    >
                    <td>{train.trainLocations[0].location}</td>
                {/if}
            </tr>
        {/each}
    </table>
{/if}

<style>
    tr,
    th,
    td {
        border: 1px solid black;
    }
</style>
