<script>
    export let data;
</script>

{#if data}
    <table>
        <th>Value (MWh/h)</th><th>Date</th><th>Time</th>
        {#each data as r}
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
{#if data && data.length == 0}
    <p class="error">No results found for this date</p>
{/if}

<style>
    tr,
    td,
    th {
        border: 1px solid black;
    }
    .error {
        color: red;
    }
</style>
