<script>
    import { onMount } from "svelte";
    const url = "https://rata.digitraffic.fi/api/v2/graphql/graphql";
    let trains;

    //$: console.log(trains)

    function fetchData() {
        const q2 = {
            query: `{
        trainsByDepartureDate(
          departureDate: "2022-10-06"
          where: {timeTableRows: {contains: {station: {shortCode: {equals: "ROI"}}}}}
        ) {
          trainNumber
          departureDate
          timeTableRows {
            station {
              name
              uicCode
            }
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
            body: JSON.stringify(q2),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then((result) => {
                trains = result.data.trainsByDepartureDate;
                console.log(trains);
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
                <td>{train.timeTableRows[0].station.name}</td>
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
