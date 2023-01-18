import React from 'react'


const AuthorItem = ({item}) => {
    return (
        <tr>
        <td>{item.id}</td>
        <td>{item.first_name}</td>
        <td>{item.birth_year}</td>
        </tr>
    )
}

const AuthorList = ({items}) => {
    return (
        <table>
        <tr>
        <th>ID</th>
        <th>First Name</th>
        <th>Birth year</th>
        </tr>
        {items.map((item) => <AuthorItem item={item} />)}
        </table>
    )
}
export default AuthorList
