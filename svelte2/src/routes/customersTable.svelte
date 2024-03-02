<script>
    export let customers
</script>
<table>
    <tr>
    <th>Id</th><th>Name</th><th>Address</th><th>Country</th><th>Status</th><th>Age Group</th>
    </tr>
    {#each customers as customer}
        <tr>
            <td>{customer.id}</td>
            <td>{customer.name}</td>
            <td>{customer.address}</td>
            <td>{customer.country}</td>
            <td>{customer.status}</td>
            <td>{customer.agegroup}</td>
        </tr>
    {/each}
</table>
<style>
    tr, td, th {
    border: 1px solid black;
    padding: 5px;
    }
</style>