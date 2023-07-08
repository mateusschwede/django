from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
    
    # Validação (validate_campoValidacao):
    def validate_avaliacao(self, valor):
        if valor in range(1,6):
            return valor
        raise serializers.ValidationError('A avaliação precisa ser entre 1 e 5')

class CursoSerializer(serializers.ModelSerializer):
    
    # 1.Nested Relationship:
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    # 2.HyperLinked Related Field:
    #(nomeRota-função), pois endpoint será gerado automaticamente via ViewSet e Router
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    # 3.Primary Key Related Field:
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # Validação dados serializers:
    media_avaliacoes = serializers.SerializerMethodField()
    
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        )
    
    def get_media_avaliacoes(self, obj): #get_nomeAtributoAtualizante
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg') #avaliacoes vem de related_name model Curso
        if media is None:
            return 0
        return round(media*2) / 2