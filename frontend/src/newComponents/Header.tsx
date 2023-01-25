import React from 'react'
import { useLightsContext } from '../context';

export default function Header() {
    const { user } = useLightsContext();

  return (
    <div>Hello, {user.name}</div>
  )
}
