export const downloadJSON = (data: any, filename = "data.json") => {
    const dataStr = JSON.stringify(data, null, 2)
    const blob = new Blob([dataStr], { type: 'application/json' })
    const url = URL.createObjectURL(blob)

    const link = document.createElement('a')
    link.href = url
    link.download = filename
    link.click()

    URL.revokeObjectURL(url)
}

export const downloadCSV = (url: string, filename = 'data.csv') => {
    const link = document.createElement('a')
    link.href = url
    link.download = filename
    link.click()
}