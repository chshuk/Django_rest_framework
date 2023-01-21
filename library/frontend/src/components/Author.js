import React from 'react'
import {Link} from 'react-router-dom'


const AuthorItem = ({item}) => {
    return (
        <tr>
        <td><Link to={`author/${item.id}`}> {item.id} </Link></td>
        <td> {item.first_name} {item.last_name} </td>
        <td> {item.birth_year} </td>
        </tr>
    )
}

const AuthorList = ({items}) => {
    return (
        <table>
        <tr>
        <th> ID </th>
        <th> Name </th>
        <th> Birth year </th>
        </tr>
        {items.map((item) => <AuthorItem item={item} />)}
        </table>
    )
}
export default AuthorList
