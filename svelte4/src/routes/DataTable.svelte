<script>
    export let windData;
</script>

{#if !windData}
    <table class="emptytable">
        <h2>Choose a date to dispaly data table</h2>
    </table>
{/if}
{#if windData}
    <h3>Wind power generation in Finland</h3>
    <table>
        <th>Value (MWh/h)</th><th>Date</th><th>Time</th>
        {#each windData as r}
            <tr>
                <td>{r.value}</td>
                <td
                    >{r.startTime.getDate()}.{r.startTime.getMonth() + 1}.
                    {r.startTime.getFullYear()}</td
                >
                <td>{r.startTime.getHours()}:{r.startTime.getMinutes()}0</td>
            </tr>
        {/each}
    </table>
{/if}
{#if windData && windData.length == 0}
    <p class="error">No results found for this date</p>
{/if}

<style>
    h2 {
        color: black;
        background-color: moccasin;
        border-radius: 3px;
        padding: 10px;
        height: 1em;
    }
    .emptytable {
        display: flex;
        justify-content: center;
        border-collapse: collapse;
        background-color: sandybrown;
        box-shadow: 5px 5px 10px black;
        width: 70rem;
        height: 50vh;
        border: 1px solid black;
    }
    table {
        border-collapse: collapse;
        background-color: goldenrod;
        box-shadow: 5px 5px 10px black;
        width: 70rem;
        height: 50vh;
        margin-bottom: 5rem;
    }
    tr,
    td,
    th {
        border: 1px solid black;
    }
    tr:nth-child(even) {
        background-color: sandybrown;
    }
    .error {
        color: red;
    }
</style>
