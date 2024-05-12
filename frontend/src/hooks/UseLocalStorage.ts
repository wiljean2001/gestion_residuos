import { atom } from "nanostores"
import { useEffect, useState } from "react"

interface LocalStorageProps<T> {
	key: string
	defaultValue: T
}

/**
 * Using local storage with useEffect
 * @param key
 * @param default
 * @returns [storedValue, setStoredValue]
 */
export default function useLocalStorage<T>({
	key,
	defaultValue
}: LocalStorageProps<T>) {
	const [value, setValue] = useState<T>(() => {
		const storedValue = localStorage.getItem(key)
		return storedValue !== null ? (JSON.parse(storedValue) as T) : defaultValue
	})

	useEffect(() => {
		localStorage.setItem(key, JSON.stringify(value))
	}, [value, key])

	return [value, setValue] as const
}

export function useLocalStorageSave<T>(key: string, value: T) {
	const isBrowser = typeof window !== "undefined"

	isBrowser && (localStorage.setItem(key, JSON.stringify(value)) as T)
}
export function useLocalStorageGet<T>(key: string) {
	const isBrowser = typeof window !== "undefined"
	return isBrowser
		? (JSON.parse(localStorage.getItem(key) as string) as T)
		: null
}
