// A custom hook for get pathname
import { useEffect, useState } from "react"

export const usePathname = () => {
	const [pathname, setPathname] = useState("")

	useEffect(() => {
		// Asegurarse de que este código se ejecuta solo en el cliente
		setPathname(window.location.pathname)
	}, [])

	return [pathname, setPathname] as const
}
