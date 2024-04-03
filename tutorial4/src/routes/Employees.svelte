<script>
    let employees = [];
    fetch("http://localhost:5000/employees")
        .then((response) => response.json())
        .then((json) => {
            employees = json;
        });
</script>

<h1>Employees</h1>
{#if employees.length}
    <table>
        <tr>
            <th>Emp no</th>
            <th>First Name</th>
            <th>Last Name</th>
        </tr>
        {#each employees as emp}
            <tr>
                <td>{emp.employeeNumber}</td>
                <td>{emp.firstName}</td>
                <td>{emp.lastName}</td>
            </tr>
        {/each}
    </table>
{/if}

<style>
    h1 {
        font-family: "Arial", sans-serif;
        text-align: center;
        color: black;
        border: 1px solid black;
        box-shadow: 5px 5px 15px black;
        background-color: moccasin;
    }
    table {
        border-collapse: collapse;
        background-color: goldenrod;
        box-shadow: 5px 5px 15px black;
        width: 100%;
    }
    tr,
    th,
    td {
        border: 1px solid black;
    }
    tr:nth-child(even) {
        background-color: moccasin;
    }
</style>
