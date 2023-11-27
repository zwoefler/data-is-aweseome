import { describe, expect, test } from 'vitest'
import { parseTimestamp } from 'utils/parkhouseData.js'

describe('parseTimestamp', async () => {
    test('returns a valid Date Object', () => {
        const timestamp = "21022023-0900"
        const result = parseTimestamp(timestamp)
        expect(result).toBeInstanceOf(Date)
    })
})