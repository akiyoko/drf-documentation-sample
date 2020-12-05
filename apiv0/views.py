from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status, views
from rest_framework.response import Response

from shop.models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(views.APIView):
    """本モデルの取得（一覧）・登録APIクラス"""

    @extend_schema(
        responses={200: BookSerializer},
    )
    def get(self, request, *args, **kwargs):
        """本モデルの取得（一覧）APIに対応するハンドラメソッド"""

        # モデルオブジェクトの一覧を取得
        book_list = Book.objects.all()
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book_list, many=True)
        # レスポンスオブジェクトを返す
        return Response(serializer.data, status.HTTP_200_OK)

    @extend_schema(
        request=BookSerializer,
        responses={201: BookSerializer},
    )
    def post(self, request, *args, **kwargs):
        """本モデルの登録APIに対応するハンドラメソッド"""

        # シリアライザオブジェクトを作成
        serializer = BookSerializer(data=request.data)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを登録
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_201_CREATED)


class BookRetrieveUpdateDestroyAPIView(views.APIView):
    """本モデルの取得（詳細）・更新・一部更新・削除APIクラス"""

    def get(self, request, pk, *args, **kwargs):
        """本モデルの取得（詳細）APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        """本モデルの更新APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを更新
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        """本モデルの一部更新APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを一部更新
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        """本モデルの削除APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # モデルオブジェクトを削除
        book.delete()
        # レスポンスオブジェクトを作成して返す
        return Response(status=status.HTTP_204_NO_CONTENT)
