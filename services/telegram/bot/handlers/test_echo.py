from aiogram import types, Router

router = Router()


@router.message()
async def echo(message: types.Message) -> None:
    await message.answer(message.text)
