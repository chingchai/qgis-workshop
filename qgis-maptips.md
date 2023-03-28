# Basic HTML Code for Map Tips
```html
<style>
body {background-color: #dddddd!important; font-family: sans-serif;}
table {border-collapse: collapse;}
tr {border: 2px solid white;}
td {white-space: nowrap; padding: 5px;}
td.bold {font-weight: bold;}
td.gap {background-color:white;padding:1px;}
</style>

<table style="width:100%">
<th colspan=1><h1>Title1</h1></th>
<tr><td class="bold">Title2:</td><td> [% "column 1" %] [% "column 1" %] </td></tr>
<tr><td class="bold">Title3:</td><td> [% "column 3" %] </td></tr>
<tr><td class="gap"></td><td class="gap"></td></tr>
<tr><td class="bold">Title4:</td><td>[% "column 4" %]</td></tr>
</table>
```
